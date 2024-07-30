import { Routes } from '@angular/router';
import { ReportesComponent } from './reportes/reportes.component';
import { MovimientosComponent } from './movimientos/movimientos.component';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { CrearCuentaComponent } from './crear-cuenta/crear-cuenta.component';
import { SocioComponent } from './socio/socio.component';
import { RegistroComponent } from './registro/registro.component';

export const routes: Routes = [
    { path: '', redirectTo: 'home', pathMatch: 'full' },
    { path: 'reportes', component: ReportesComponent },
    { path: 'movimientos', component: MovimientosComponent },
    { path: 'login', component: LoginComponent },
    { path: 'home', component: HomeComponent },
    { path: 'crear-cuenta', component: CrearCuentaComponent },
    { path: 'socio', component: SocioComponent },
    { path: 'registro', component: RegistroComponent },
];