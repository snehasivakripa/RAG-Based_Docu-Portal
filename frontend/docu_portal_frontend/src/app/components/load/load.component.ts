import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
@Component({
  selector: 'app-load',
  standalone: true,
  imports: [CommonModule,FormsModule, HttpClientModule],
  templateUrl: './load.component.html',
  styleUrl: './load.component.css'
})

export class LoadComponent {
  url = '';
  message = '';

  constructor(private api: ApiService) {}

  load() {
    this.api.loadData([this.url]).subscribe({
      next: res => this.message = res.message,
      error: err => this.message = err.error.error || 'Error loading data'
    });
  }
}
