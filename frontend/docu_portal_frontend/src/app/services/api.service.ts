import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root' 
})
export class ApiService {
  private BASE_URL = 'http://127.0.0.1:5000/api';

  constructor(private http: HttpClient) {}

  loadData(urls: string[]): Observable<any> {
    return this.http.post(`${this.BASE_URL}/load`, { urls });
  }

  uploadPdf(formData: FormData): Observable<any> {
  return this.http.post(`${this.BASE_URL}/upload_pdf`, formData);
}

  queryData(query: string): Observable<any> {
    return this.http.post(`${this.BASE_URL}/query`, { query });
  }
}
