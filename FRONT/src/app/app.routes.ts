import { Routes } from '@angular/router';
import { AddTutorialComponent } from './components/add-tutorial/add-tutorial.component';
import { TutorialDetailsComponent } from './components/tutorial-details/tutorial-details.component';
import { TutorialsListComponent } from './components/tutorials-list/tutorials-list.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';

export const routes: Routes = [

    { path: 'add-tutorial', component: AddTutorialComponent },
    { path: 'tutorial-details', component: TutorialDetailsComponent },
    { path: 'tutorial-list', component: TutorialsListComponent },
    // { path: '', redirectTo: '/login', pathMatch: 'full' },
    { path: '', redirectTo: '/add-tutorial', pathMatch: 'full' },
    { path: 'register', component: RegisterComponent },
    { path: 'login', component: LoginComponent },
    { path: '**', redirectTo: '/add-tutorial' }
    
];
