$(document).ready(function () {

    let cropper = null;
    var imgArray = [];
    var imgGuardadas = [];
    var con = 0;
    var file_actual = ""
    var conCal = 0


    function croppeR(file) {
        file_actual = file
        let image = document.getElementById('img-cropper')
        let input = document.getElementById(file)
        let archivos = input.files

        if (!archivos || !archivos.length) {
            image.src = "";
            input.value = "";

        } else {
            let imagenUrl = URL.createObjectURL(archivos[0])
            image.src = imagenUrl

            cropper = new Cropper(image, {
                checkOrientation: true,
                cropBoxMovable: false,
                cropBoxResizable: false,
                toggleDragModeOnDblclick: false,
                modal: true,
                guides: false,
                center: false,
                rotatable: true,
                guides: false,
                highlight: false,
                aspectRatio: 1.8, // es la proporción en la que queremos que recorte en este caso
                zoomable: true, //Para que haga zoom 
                viewMode: 0, //Para que no estire la imagen al contenedor
                responsive: false, //Para que no reacomode con zoom la imagen al contenedor
                dragMode: 'move', //Para que al arrastrar no haga nada
                ready() { // metodo cuando cropper ya este activo, le ponemos el alto y el ancho del contenedor de cropper al 100%
                    document.querySelector('.cropper-container').style.width = '100%'
                    document.querySelector('.cropper-container').style.height = '100%'
                }
            })


            $('.modal-cropp').addClass('active')
            $('.modal-content-cropp').addClass('active')

            $('.modal-cropp').removeClass('remove')
            $('.modal-content-cropp').removeClass('remove')
        }
    }

    function cargarImgGuardadas(validacion) {
        if (conCal == 0) {
            conCal = 1;
            let cantidadImg = document.getElementById('cantidadImg').value
            let preview = document.getElementById('preview-images');
            for (var i = 0; i < cantidadImg; i++) {
                let imgCom = document.getElementById('imgComprov' + i);
                let rutaimg = imgCom.src
                const xhr = new XMLHttpRequest();
                xhr.open('GET', rutaimg, true);
                xhr.responseType = 'blob';
                xhr.onload = function () {
                    if (this.status === 200) {
                        const blobImagen = this.response;
                        const fileReader = new FileReader();
                        fileReader.readAsDataURL(blobImagen);
                        fileReader.onload = function () {
                            const base64Imagen = fileReader.result;
                            if (i == 0) imgGuardadas[0] = { rutaA: imgCom.src, rutaB: base64Imagen }
                            else {
                                imgGuardadas[imgGuardadas.length] = { rutaA: imgCom.src, rutaB: base64Imagen }
                            }
                            imgArray[imgArray.length] = base64Imagen
                        };
                    }
                };
                xhr.send();
                if(validacion==1){
                    let divImg = document.createElement('div');
                    divImg.classList.add('thumbnail', i);
                    divImg.setAttribute('id', i)
                    let createImg = document.createElement('img');
                    createImg.setAttribute('class', i);
                    createImg.setAttribute('src', rutaimg);
                    createImg.setAttribute('id', 'img' + i)
                    preview.appendChild(divImg);
                    let previewImg = document.getElementById(i);
                    previewImg.appendChild(createImg)
                    var closeButton = document.createElement('div');
                    closeButton.classList.add('close-button');
                    closeButton.setAttribute('id', i);
                    closeButton.setAttribute('name', 'file_comprovantes')
                    closeButton.innerHTML = 'x';
                    document.getElementsByClassName(i)[0].appendChild(closeButton);
                }
            }
        }
    }

    $('#file').on('change', () => {
        imgArray.forEach(function (imagen) {
            if (imagen != "ninguna") {
                con = 1;
            }
        })
        if (con == 0) {
            croppeR("file");

        } else {
            // alert("Solo se puede subir un radicado")
            Swal.fire(
                'Solo puedes subir una sola imagen',
                'Para cambiar la imagen actual primero tiene que descartar la actual',
                'error'
            )
            let image = document.getElementById('img-cropper')
            let input = document.getElementById('file')

            image.src = "";
            input.value = "";
        }
    })

    $('#file_comprovantes').on('change', () => {
        cargarImgGuardadas(0)
        croppeR("file_comprovantes");
    })


    $('#close').on('click', () => {
        let image = document.getElementById('img-cropper')
        let input = document.getElementById(file_actual)

        image.src = "";
        input.value = "";
        con = 0;

        cropper.destroy()

        $('.modal-cropp').addClass('remove')
        $('.modal-content-cropp').addClass('remove')

        $('.modal-cropp').removeClass('active')
        $('.modal-content-cropp').removeClass('active')
    })

    $('#cut').on('click', () => {
        let canva = cropper.getCroppedCanvas({
            width: 1920,
            height: 1080,
        });
        let image = document.getElementById('img-cropper')
        let input = document.getElementById(file_actual)
        let preview = document.getElementById('preview-images');
        const canvas = document.createElement('canvas'); // Crear un elemento canvas
        const ctx = canvas.getContext('2d');
        canvas.width = 1920; // Establecer el ancho del canvas
        canvas.height = 1080; // Establecer la altura del canvas
        var imagen = new Image(); // Crear un elemento img y asignarle la URL del objeto blob
        ctx.drawImage(imagen, 0, 0); // Dibujar la imagen en el canvas
        canva.toBlob(function (blob) {
            const fileReader = new FileReader(); // Crear un objeto FileReader
            fileReader.readAsDataURL(blob); // Convertir el blob a base64
            fileReader.onloadend = function () {
                const base64data = fileReader.result; // Obtener la URL base64 de la imagen JPEG
                imgArray[imgArray.length] = base64data;
                let divImg = document.createElement('div');
                divImg.classList.add('thumbnail', imgArray.length - 1);
                divImg.setAttribute('id', imgArray.length - 1)
                let createImg = document.createElement('img');
                createImg.setAttribute('class', imgArray.length - 1);
                createImg.setAttribute('src', base64data);
                createImg.setAttribute('id', 'img' + imgArray.length - 1)
                preview.appendChild(divImg);
                let previewImg = document.getElementById(imgArray.length - 1);
                previewImg.appendChild(createImg)
                var closeButton = document.createElement('div');
                closeButton.classList.add('close-button');
                closeButton.setAttribute('id', imgArray.length - 1);
                closeButton.setAttribute('name', file_actual)
                closeButton.innerHTML = 'x';
                document.getElementsByClassName(imgArray.length - 1)[0].appendChild(closeButton);
            }
        }, 'image/jpeg', 0.8);
        image.src = "";
        input.value = "";
        cropper.destroy()

        $('.modal-cropp').addClass('remove')
        $('.modal-content-cropp').addClass('remove')

        $('.modal-cropp').removeClass('active')
        $('.modal-content-cropp').removeClass('active')

    })


    $('#rotarD').on('click', () => {  //boton para girar a la derecha
        cropper.rotate(90);
    })
    $('#rotarI').on('click', () => {  //boton para girar a la izquierda
        cropper.rotate(-90);
    })

    document.body.addEventListener('click', async function (e) {
        if (e.target.classList.contains('close-button')) {
            const id = e.target.getAttribute("id");//obteniendo la id es el indice de donde esta imagen en el array
            const imagen = document.getElementById('img' + id);
            var rutabase64 = '';
            e.target.parentNode.remove();    //remuevo el div padre de donde se visualisa la imagen
            var nameValue = e.target.getAttribute('name');
            // alert(nameValue)
            if(nameValue=="file"){
                imgArray[id]="ninguna"
            }else{
                for (j = 0; j < imgGuardadas.length; j++) {
                    if (imgGuardadas[j].rutaA == imagen.src) {
                        rutabase64 = imgGuardadas[j].rutaB
                    }
                    const formData = new FormData();
                    // alert(imgGuardadas[j].rutaA)
                    formData.append("ruta", imgGuardadas[j].rutaA);
                    // Enviar la solicitud HTTP al servidor de Python
                    fetch("/eliminarImgEvento", {
                        method: "POST",
                        body: formData
                    });
                    imgGuardadas[j] = "ninguna"
                }
                // console.log(imgArray.length)
                for (j = 0; j < imgArray.length; j++) {
                    if (imgArray[j] == rutabase64) {
                        // alert(rutabase64)
                        imgArray[j] = "ninguna"
                    }
                }
            }
            con = 0;
        }
    })
    $('#enviarB').on('click', () => {
        cont = 0;

        // var inputNombre = document.getElementById("code");
        // Obtener el valor actual del campo de entrada
        var codigo = "";
        // Obtén una referencia al elemento select
        const selectElement = document.getElementById('productPlaze').value;
        codigo=selectElement

        imgArray.forEach(function (imagen) {
            if (imagen != "ninguna" && cont == 0) {
                cont++;
                const formData = new FormData();
                formData.append("imagen", imagen);
                // formData.append("num",cont)
                formData.append("codigo", codigo)
                // Enviar la solicitud HTTP al servidor de Python
                fetch("/saveImg", {
                    method: "POST",
                    body: formData
                });
            }
        })

        console.log(cont)
        // document.getElementById("num_fotos").value = cont;

    })
    $('#edit-boton').on('click', () => {
        cont = 0;

        // var inputNombre = document.getElementById("code");
        // Obtener el valor actual del campo de entrada
        var codigo = document.getElementById("codigoEvento").value;
        imgArray.forEach(function (imagen) {
            if (imagen != "ninguna") {
                cont++;
                const formData = new FormData();
                formData.append("imagen", imagen);
                formData.append("num", cont)
                formData.append("codigo", codigo)
                // Enviar la solicitud HTTP al servidor de Python
                fetch("/guardarImgEvento", {
                    method: "POST",
                    body: formData
                });
            }
        })

        console.log(cont)
        // document.getElementById("num_fotos").value = cont;

    })
    $('#btn-eliminar-comprovantes').on('click', () => {
        cargarImgGuardadas(1)
    })
})
