import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { ApiService } from '../../core/services/api.service';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent {
  user = {
    username: '',
    email: '',
    password: ''
  };
  errorMessage: string = '';

  constructor(private apiService: ApiService, private router: Router) {}

  onSubmit(): void {
    this.register();
  }

  register(): void {
    this.apiService.post<any>('api/auth/register/', this.user).subscribe({
      next: (res) => {
        console.log('Registration successful:', res);
        this.router.navigate(['/login']);
      },
      error: (err) => {
        console.error('Registration error:', err);
        this.errorMessage = 'Registration failed. Please try again.';
      }
    });
  }
}