import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ApiService } from '../../core/services/api.service';
import { Tutorial } from '../../shared/models/tutorial.model';

@Component({
  selector: 'app-tutorials-list',
  standalone: true,
  imports: [CommonModule, RouterModule], // RouterModule для ссылок
  templateUrl: './tutorials-list.component.html',
  styleUrls: ['./tutorials-list.component.scss']
})
export class TutorialsListComponent implements OnInit {
  tutorials: Tutorial[] = [];
  publishedTutorials: Tutorial[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.getAllTutorials();
    this.getPublishedTutorials();
  }

  getAllTutorials(): void {
    this.apiService.get<any[]>('api/tutorials').subscribe({
      next: (data) => this.tutorials = data.map(t => ({ id: t.pk, ...t.fields })),
      error: (err) => console.error('Error fetching tutorials:', err)
    });
  }

  getPublishedTutorials(): void {
    this.apiService.get<any[]>('api/tutorials/published').subscribe({
      next: (data) => this.publishedTutorials = data.map(t => ({ id: t.pk, ...t.fields })),
      error: (err) => console.error('Error fetching published tutorials:', err)
    });
  }
}