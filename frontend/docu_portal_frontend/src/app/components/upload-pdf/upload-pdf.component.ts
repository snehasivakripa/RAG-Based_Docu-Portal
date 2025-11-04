import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
@Component({
  selector: 'app-upload-pdf',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './upload-pdf.component.html',
  styleUrl: './upload-pdf.component.css'
})
export class UploadPdfComponent {
  selectedFile: File | null = null;
  pdfMessage: string = '';

  constructor(private api: ApiService) {}

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  uploadPdf() {
    if (!this.selectedFile) {
      this.pdfMessage = 'Please select a PDF file.';
      return;
    }

    const formData = new FormData();
    formData.append('file', this.selectedFile);

    this.api.uploadPdf(formData).subscribe({
      next: res => this.pdfMessage = res.message,
      error: err => this.pdfMessage = err.error?.error || 'Error uploading PDF'
    });
  }
}
