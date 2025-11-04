import { Component } from '@angular/core';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
@Component({
  selector: 'app-query',
  standalone: true,
   imports: [CommonModule,FormsModule,HttpClientModule],
  templateUrl: './query.component.html',
  styleUrl: './query.component.css'
})

export class QueryComponent {
  query = '';
  results: string[] = [];

  constructor(private api: ApiService) {}

  ask() {
    this.api.queryData(this.query).subscribe({
      next: res => this.results = res.results,
      error: err => this.results = ['Error: ' + err.error.error]
    });
  }
}
