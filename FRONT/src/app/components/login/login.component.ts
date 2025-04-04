import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { ApiService } from '../../core/services/api.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
  username: string = '';
  password: string = '';
  errorMessage: string = '';

  constructor(private apiService: ApiService, private router: Router) {}

  login(): void {
    const credentials = { username: this.username, password: this.password };
    this.apiService.post<any>('api/auth/login/', credentials).subscribe({
      next: (res) => {
        console.log('Login successful:', res);
        // Сохранение токенов и перенаправление на другую страницу
        localStorage.setItem('access_token', res.access);
        localStorage.setItem('refresh_token', res.refresh);
        this.router.navigate(['/tutorial-list']);
      },
      error: (err) => {
        console.error('Login error:', err);
        this.errorMessage = 'Invalid username or password';
      }
    });
  }
}
