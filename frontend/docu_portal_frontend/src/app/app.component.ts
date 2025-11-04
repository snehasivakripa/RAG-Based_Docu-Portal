import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { LoadComponent } from './components/load/load.component';
import { QueryComponent } from './components/query/query.component';
import { UploadPdfComponent } from './components/upload-pdf/upload-pdf.component';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, LoadComponent,UploadPdfComponent, QueryComponent,HttpClientModule ],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'advanced_chatbot';
}
