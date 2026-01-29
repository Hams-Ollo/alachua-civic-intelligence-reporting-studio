"""
Docling document processor for Alachua Civic Intelligence System.

Provides document parsing and chunking for:
- PDF files (staff reports, agendas, application materials)
- DOCX files
- Other document formats supported by Docling

Integrates with LangChain for text splitting.
"""

import os
from pathlib import Path
from typing import Optional, Union
from dataclasses import dataclass

from docling.document_converter import DocumentConverter
from langchain.text_splitter import RecursiveCharacterTextSplitter


@dataclass
class ProcessedDocument:
    """Result from document processing."""
    source: str
    markdown: str
    chunks: list[str]
    success: bool
    error: Optional[str] = None
    metadata: Optional[dict] = None


class DoclingProcessor:
    """
    Document processor using Docling for parsing and LangChain for chunking.
    
    Usage:
        processor = DoclingProcessor()
        result = processor.process_pdf("staff_report.pdf")
        for chunk in result.chunks:
            print(chunk)
    """
    
    def __init__(
        self,
        chunk_size: int = 512,
        chunk_overlap: int = 50,
        separators: list[str] = None
    ):
        """
        Initialize document processor.
        
        Args:
            chunk_size: Target size for text chunks (characters)
            chunk_overlap: Overlap between chunks
            separators: Custom separators for splitting (default: paragraph, line, sentence, word)
        """
        self.converter = DocumentConverter()
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separators = separators or ["\n\n", "\n", ". ", " "]
        
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=self.separators
        )
    
    def process_file(self, file_path: Union[str, Path]) -> ProcessedDocument:
        """
        Process a local file (PDF, DOCX, etc.).
        
        Args:
            file_path: Path to the document file
        
        Returns:
            ProcessedDocument with markdown and chunks
        """
        file_path = Path(file_path)
        
        if not file_path.exists():
            return ProcessedDocument(
                source=str(file_path),
                markdown="",
                chunks=[],
                success=False,
                error=f"File not found: {file_path}"
            )
        
        try:
            # Convert document to Docling format
            result = self.converter.convert(str(file_path))
            
            # Export to markdown
            markdown = result.document.export_to_markdown()
            
            # Chunk the markdown
            chunks = self.splitter.split_text(markdown)
            
            return ProcessedDocument(
                source=str(file_path),
                markdown=markdown,
                chunks=chunks,
                success=True,
                metadata={
                    "num_chunks": len(chunks),
                    "total_chars": len(markdown),
                    "file_type": file_path.suffix
                }
            )
            
        except Exception as e:
            return ProcessedDocument(
                source=str(file_path),
                markdown="",
                chunks=[],
                success=False,
                error=str(e)
            )
    
    def process_url(self, url: str) -> ProcessedDocument:
        """
        Process a document from URL (PDF, etc.).
        
        Args:
            url: URL to the document
        
        Returns:
            ProcessedDocument with markdown and chunks
        """
        try:
            # Docling can handle URLs directly
            result = self.converter.convert(url)
            
            # Export to markdown
            markdown = result.document.export_to_markdown()
            
            # Chunk the markdown
            chunks = self.splitter.split_text(markdown)
            
            return ProcessedDocument(
                source=url,
                markdown=markdown,
                chunks=chunks,
                success=True,
                metadata={
                    "num_chunks": len(chunks),
                    "total_chars": len(markdown)
                }
            )
            
        except Exception as e:
            return ProcessedDocument(
                source=url,
                markdown="",
                chunks=[],
                success=False,
                error=str(e)
            )
    
    def process_bytes(self, content: bytes, filename: str = "document.pdf") -> ProcessedDocument:
        """
        Process document from bytes (e.g., downloaded content).
        
        Args:
            content: Document content as bytes
            filename: Filename hint for format detection
        
        Returns:
            ProcessedDocument with markdown and chunks
        """
        import tempfile
        
        try:
            # Write to temp file for Docling
            suffix = Path(filename).suffix or ".pdf"
            with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
                tmp.write(content)
                tmp_path = tmp.name
            
            try:
                result = self.process_file(tmp_path)
                result.source = filename
                return result
            finally:
                # Clean up temp file
                os.unlink(tmp_path)
                
        except Exception as e:
            return ProcessedDocument(
                source=filename,
                markdown="",
                chunks=[],
                success=False,
                error=str(e)
            )
    
    def extract_tables(self, file_path: Union[str, Path]) -> list[str]:
        """
        Extract tables from a document as markdown.
        
        Args:
            file_path: Path to the document
        
        Returns:
            List of tables as markdown strings
        """
        try:
            result = self.converter.convert(str(file_path))
            
            tables = []
            for element in result.document.elements:
                if hasattr(element, 'type') and 'table' in str(element.type).lower():
                    if hasattr(element, 'export_to_markdown'):
                        tables.append(element.export_to_markdown())
                    else:
                        tables.append(str(element))
            
            return tables
            
        except Exception as e:
            print(f"Error extracting tables: {e}")
            return []
    
    def chunk_text(self, text: str) -> list[str]:
        """
        Chunk arbitrary text using configured splitter.
        
        Args:
            text: Text to chunk
        
        Returns:
            List of text chunks
        """
        return self.splitter.split_text(text)
