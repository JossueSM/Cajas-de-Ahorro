import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-socio',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './socio.component.html',
  styleUrl: './socio.component.css'
})
export class SocioComponent {
  form_socio: FormGroup;
  socio: any;

  crear_socio(){
    const id_usuario = this.form_socio.get("id_usuario")?.value;
    const estado_socio = this.form_socio.get("estado_socio")?.value == 'true';

    fetch('http://localhost:5000/socio', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        id_usuario: id_usuario,
        estado_socio: estado_socio,
      })
    })
      .then(response => response.json())
      .then(data => {
          console.log(data["mensaje"], data["Socio"]);
          this.socio = data["Socio"]
      })
      .catch(error => console.error('Error al crear la cuenta del usuario', error));
  }

  constructor(private fb: FormBuilder){
    this.form_socio = this.fb.group({
      id_usuario: ['', Validators.required],
      estado_socio: ['', Validators.required]
    })
  }
}
