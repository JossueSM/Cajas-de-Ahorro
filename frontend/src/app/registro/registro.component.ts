import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-registro',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './registro.component.html',
  styleUrl: './registro.component.css'
})
export class RegistroComponent {
  form_registro: FormGroup;
  registro: any;

  registrar_usuario(){
    const cedula = this.form_registro.get("cedula")?.value;
    const email = this.form_registro.get("email")?.value;
    const user = this.form_registro.get("user")?.value;
    const password = this.form_registro.get("password")?.value;

    fetch('http://localhost:5000/usuario', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        id_usuario: cedula,
        email_usuario: email,
        nombre_usuario: user,
        password_usuario: password
      })
    })
      .then(response => response.json())
      .then(data => {
          console.log(data["mensaje"], data["Usuario"]);
          this.registro = data["Usuario"]
      })
      .catch(error => console.error('Error al crear el usuario', error));
  }

  constructor(private fb: FormBuilder){
    this.form_registro = this.fb.group({
      cedula: ['', Validators.required], 
      email: ['', Validators.required],
      user: ['', Validators.required],
      password: ['', Validators.required]
    })
  }
}
