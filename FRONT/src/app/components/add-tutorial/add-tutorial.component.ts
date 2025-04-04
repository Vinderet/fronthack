import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../core/services/api.service';
import { Tutorial } from '../../shared/models/tutorial.model';

@Component({
  selector: 'app-add-tutorial',
  standalone: true,
  imports: [CommonModule, FormsModule], // Импорты для работы с формами и *ngIf
  templateUrl: './add-tutorial.component.html',
  styleUrls: ['./add-tutorial.component.scss']
})
export class AddTutorialComponent {
  tutorial: Tutorial = {
    title: '',
    description: '',
    published: false,
    fields: undefined
  };
  submitted = false;

  constructor(private apiService: ApiService) {}

  saveTutorial(): void {
    this.apiService.post<Tutorial>('api/tutorials/', this.tutorial).subscribe({
      next: (res) => {
        console.log('Tutorial added:', res);
        this.submitted = true;
        this.resetForm();
      },
      error: (err) => console.error('Error adding tutorial:', err)
    });
  }

  resetForm(): void {
    this.tutorial = { title: '', description: '', published: false, fields: undefined };
    this.submitted = false;
  }
}