import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-crear-cuenta',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './crear-cuenta.component.html',
  styleUrl: './crear-cuenta.component.css'
})
export class CrearCuentaComponent {

  form_cuenta: FormGroup;
  // numero_cuenta: String = '';
  // tipo_cuenta: String = '';
  // saldo_cuenta: number = 0;
  // id_usuario: String = '';

  crearCuenta() {

    const numero_cuenta = this.form_cuenta.get("numero_cuenta")?.value;
    const tipo_cuenta = this.form_cuenta.get("tipo_cuenta")?.value;
    const saldo_cuenta = this.form_cuenta.get("saldo_cuenta")?.value;
    const id_usuario = this.form_cuenta.get("id_usuario")?.value;

    fetch('http://localhost:5000/cuenta', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        numero_cuenta: numero_cuenta,
        tipo_cuenta: tipo_cuenta,
        saldo_cuenta: saldo_cuenta,
        id_usuario: id_usuario
      })
    })
      .then(response => response.json())
      .then(data => console.log(data["mensaje"], data["Cuenta"]))
      .catch(error => console.error('Error al crear la cuenta del usuario', error));
  }

  constructor(private fb: FormBuilder){
    this.form_cuenta = this.fb.group({
      numero_cuenta: ['', Validators.required],
      tipo_cuenta: ['', Validators.required],
      saldo_cuenta: ['', Validators.required],
      id_usuario: ['', Validators.required],
    })
  }
}
