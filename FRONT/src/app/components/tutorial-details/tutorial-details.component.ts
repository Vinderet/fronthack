import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, RouterModule } from '@angular/router';
import { ApiService } from '../../core/services/api.service';
import { Tutorial } from '../../shared/models/tutorial.model';

@Component({
  selector: 'app-tutorial-details',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule], // Добавляем RouterModule для маршрутов
  templateUrl: './tutorial-details.component.html',
  styleUrls: ['./tutorial-details.component.scss']
})
export class TutorialDetailsComponent implements OnInit {
  tutorial: Tutorial | null = null;

  constructor(
    private apiService: ApiService,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.getTutorial(+id);
    }
  }

  getTutorial(id: number): void {
    this.apiService.get<Tutorial>(`api/tutorials/${id}`).subscribe({
      next: (data) => this.tutorial = { id, ...data },
      error: (err) => console.error('Error fetching tutorial:', err)
    });
  }

  updateTutorial(): void {
    if (this.tutorial?.id) {
      this.apiService.put<Tutorial>(`api/tutorials/${this.tutorial.id}`, this.tutorial).subscribe({
        next: () => console.log('Tutorial updated'),
        error: (err) => console.error('Error updating tutorial:', err)
      });
    }
  }

  deleteTutorial(): void {
    if (this.tutorial?.id) {
      this.apiService.delete(`api/tutorials/${this.tutorial.id}`).subscribe({
        next: () => {
          console.log('Tutorial deleted');
          this.tutorial = null;
        },
        error: (err) => console.error('Error deleting tutorial:', err)
      });
    }
  }
}