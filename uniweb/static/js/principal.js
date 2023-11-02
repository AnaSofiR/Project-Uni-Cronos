const contenedorMateria = document.querySelector('#dinamic')
const btnAgregarMateria = document.querySelector('#agregar_materia')
const contenedorProfesor1 = document.querySelector('#dinamic2')
const btnAgregarProfesor1 = document.querySelector('#agregar_profesor1')
const contenedorProfesor2 = document.querySelector('#dinamic3')
const btnAgregarProfesor2 = document.querySelector('#agregar_profesor2')

const btnGuardarDatos = document.querySelector('#guardar_datos');
const horariosJsonInput = document.querySelector('#horarios_json')
const materiasJsonInput = document.querySelector('#materias_json');
const profesorNJsonInput = document.querySelector('#profesores1_json');
const profesorSJsonInput = document.querySelector('#profesores2_json');


let total_materias = 2;
let total_profesoresN = 2;
let total_profesoresS = 2;

let horarioN = [];
let materias_seleccionadas = [];
let profesoresN = [];
let profesoresS = [];



//--------------------------MATERIAS--------------------------
//agregar materias
btnAgregarMateria.addEventListener('click', e => {
    let div = document.createElement('div');
    div.innerHTML = `<input type="text" name="materia" id="materia" placeholder="Materia" required><button onclick="eliminar(this)">Eliminar</button><ul class="list"></ul> `;
    contenedorMateria.appendChild(div);
})

//eliminar materia
const eliminar  = (e) => {
    const divPadre = e.parentNode;
    contenedorMateria.removeChild(divPadre);
    actualizarContador();
}

//actualizar contador
const actualizarContador = () => {
    let divs = contenedorMateria.children;
    total_materias = 1;
    for (let i = 0; i<divs.length; i++){
        divs[i].children[0].innerHTML = total_materias++;
    }
}


//--------------------------HORARIOS NO DISPONIBLES--------------------------



//--------------------------PROFESORES NO--------------------------

btnAgregarProfesor1.addEventListener('click', e => {
    let div = document.createElement('div');
    div.innerHTML = ` <input type="text" name="profesor1" id="profesor1" placeholder="Profesor" required><button onclick="eliminarProfesor1(this)">Eliminar</button><ul class="list"></ul> `;
    contenedorProfesor1.appendChild(div);
})

//eliminar materia
const eliminarProfesor1  = (e) => {
    const divPadre = e.parentNode;
    contenedorProfesor1.removeChild(divPadre);
    actualizarContadorProfesores1();
}

//actualizar contador
const actualizarContadorProfesores1 = () => {
    let divs = contenedorProfesor1.children;
    total_profesoresN = 1;
    for (let i = 0; i<divs.length; i++){
        divs[i].children[0].innerHTML = total_profesoresN++;
    }
}



//--------------------------PROFESORES SÍ--------------------------

btnAgregarProfesor2.addEventListener('click', e => {
    let div = document.createElement('div');
    div.innerHTML = ` <input type="text" name="profesor2" id="profesor2" placeholder="Profesor" required><button onclick="eliminarProfesor2(this)">Eliminar</button><ul class="list"></ul> `;
    contenedorProfesor2.appendChild(div);
})

//eliminar materia
const eliminarProfesor2  = (e) => {
    const divPadre = e.parentNode;
    contenedorProfesor2.removeChild(divPadre);
    actualizarContadorProfesores2();
}

//actualizar contador
const actualizarContadorProfesores2 = () => {
    let divs = contenedorProfesor2.children;
    total_profesoresS = 1;
    for (let i = 0; i<divs.length; i++){
        divs[i].children[0].innerHTML = total_profesoresS++;
    }
}

//--------------------------HORARIOS--------------------------
function reservar(dia,hora){
    const reserva = {dia,hora};
    horarioN.push(reserva);

    horariosJsonInput.value = JSON.stringify(horarioN);
    console.log(horarioN);
}




//--------------------------GUARDAR DATOS--------------------------
btnGuardarDatos.addEventListener('click', () => {
    const materia1 = document.querySelector('#materia')
    const profesorN1 = document.querySelector('#profesor1')
    const profesorS1 = document.querySelector('#profesor2')




    const divs1 = contenedorMateria.children;
    const divs2 = contenedorProfesor1.children;
    const divs3 = contenedorProfesor2.children;
    horarioN = [];
    materias_seleccionadas = [];
    profesoresN = [];
    profesoresS = [];
   

    materias_seleccionadas.push(materia1.value)
    for (let i = 0; i < divs1.length; i++) {
        const input = divs1[i].querySelector('input');
        if (input.value.trim() !== '') {
            materias_seleccionadas.push(input.value);
        }
    }
    // Almacenar las materias en el campo oculto en formato JSON
    materiasJsonInput.value = JSON.stringify(materias_seleccionadas);


    profesoresN.push(profesorN1.value)
    for (let i = 0; i < divs2.length; i++) {
        const input = divs2[i].querySelector('input');
        if (input.value.trim() !== '') {
            profesoresN.push(input.value);
        }
    }
    profesorNJsonInput.value = JSON.stringify(profesoresN) 



    profesoresS.push(profesorS1.value)
    for (let i = 0; i < divs3.length; i++) {
        const input = divs3[i].querySelector('input');
        if (input.value.trim() !== '') {
            profesoresS.push(input.value);
        }
    }
    profesorSJsonInput.value = JSON.stringify(profesoresS) 

    console.log(horarioN);
    console.log(materias_seleccionadas);
    console.log(profesoresN);
    console.log(profesoresS);

});

let materias = ["Cálculo 1",
"Principios de Desarrollo de Software",
"Fundamentos de Programación",
"Lógica",
"Introducción a la Informática",
"Programación Avanzada",
"Estadísticas", 
"Inteligencia Artificial", 
"Redes de Computadoras", 
"Programación Web", 
"Física I", 
"Matemáticas Discretas", 
"Física Moderna", 
"Introducción a la Biología", 
"Química Orgánica", 
"Introducción a la Economía", 
"Diseño Gráfico", 
"Historia de la Ciencia", 
"Psicología del Aprendizaje", 
"Química General", 
"Dibujo Técnico", 
"Psicología General", 
"Biología Celular",
"Álgebra Lineal"]

//Materias en orden ascendente
let sortedMaterias = materias.sort();

let input = document.getElementById("materia");

function eliminarDiacriticos(texto) {
  return texto.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

input.addEventListener("keyup", (e) => {
    eliminarMateria();
    let valorInput = eliminarDiacriticos(input.value).toLowerCase();
    for(let i of sortedMaterias){
        if (eliminarDiacriticos(i.toLowerCase()).startsWith(valorInput) && input.value != ""){
            let listItem = document.createElement("li");
            listItem.classList.add("list-items");
            listItem.style.cursor = "pointer";
            listItem.setAttribute("onclick", "displayMaterias('" + i +"')");
            let word =  "<b>" + i.substring(0, input.value.length) + "</b>";
            word += i.substring(input.value.length);
            listItem.innerHTML = word;
            document.querySelector(".list").appendChild(listItem);

        }
    }
});

function displayMaterias(value){
    input.value = value;
    eliminarMateria();

}
function eliminarMateria(){
    let items = document.querySelectorAll(".list-items");
    items.forEach((item) => {
        item.remove();
    });
}