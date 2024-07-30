import { Component } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-movimientos',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './movimientos.component.html',
  styleUrl: './movimientos.component.css'
})
export class MovimientosComponent {
  form_movimiento: FormGroup;
  movimiento: any;

  crear_movimiento(){
    const tipo_movimiento = this.form_movimiento.get("tipo_movimiento")?.value;
    const numero_cuenta = this.form_movimiento.get("numero_cuenta")?.value;

    fetch('http://localhost:5000/movimiento', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        tipo_movimiento: tipo_movimiento,
        numero_cuenta: numero_cuenta,
      })
    })
      .then(response => response.json())
      .then(data => {
          console.log(data["mensaje"], data["Movimiento"]);
          this.movimiento = data["Movimiento"]
      })
      .catch(error => console.error('Error al crear la cuenta del usuario', error));
  }

  constructor(private fb: FormBuilder){
    this.form_movimiento = this.fb.group({
      tipo_movimiento: ['', Validators.required],
      numero_cuenta: ['', Validators.required],
    })
  }
}
