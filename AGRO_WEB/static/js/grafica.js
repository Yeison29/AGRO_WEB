var grafica = null;
// Obtener el elemento select por su id
var harvest = document.getElementById("harvest");

function handleHarvestChange() {
  // Obtener el valor seleccionado
  var harvestvalue = harvest.value;
  pintarGrafica(harvestvalue);
}

harvest.onchange = handleHarvestChange;

let harvestData; // Variable para almacenar los datos de los usuarios

function procesarDatos() {
  // Utiliza los datos de usuariosData
  console.log(usuariosData);
  // Realiza otras operaciones con los datos
}

function pintarGrafica(harvest) {
  var datos;
  // Obtener una referencia al elemento canvas del DOM
  var $grafica = document.querySelector("#grafica");
  if (grafica !== null) {
    grafica.destroy();
  }
  fetch('/queryHarvest', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ 'harvest': harvest })
  })
    .then(response => response.json())
    .then(data => {
      // Aquí puedes procesar los datos recibidos
      console.log(data);

      var etiquetas = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
      // Podemos tener varios conjuntos de datos. Comencemos con uno
      var datosVentas2020 = {
        label: "Ventas por mes",
        data: data.arrayHarvest, // La data es un arreglo que debe tener la misma cantidad de valores que la cantidad de etiquetas
        backgroundColor: 'rgba(0, 255, 0, 0.204)', // Color de fondo
        borderColor: '#3c6a36', // Color del borde
        borderWidth: 1,// Ancho del borde
        tension: .5,
        fill: true,
      };
      var data = {
        labels: data.arrayMeses,
        datasets: [
          datosVentas2020
          // Aquí más datos...
        ]
      }
      var options = {
        animations: {
          radius: {
            duration: 400,
            easing: 'linear',
            loop: (context) => context.active
          }
        },
        hoverRadius: 12,
        hoverBackgroundColor: 'rgb(0, 255, 0)',
        interaction: {
          mode: 'nearest',
          intersect: false,
          axis: 'x'
        },
        plugins: {
          tooltip: {
            enabled: false
          },
          legend: {
            display: false, // Oculta la leyenda
          },
        }
      }
      grafica = new Chart($grafica, {
        type: 'line',// Tipo de gráfica
        data,
        options
      });


    })
    .catch(error => {
      // Maneja cualquier error que ocurra durante la solicitud
      console.error(error);
    });
  // Las etiquetas son las que van en el eje X. 
}