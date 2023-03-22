function show_register(){
    $('#form_register_user').show();
}

function hide_register(){
    $('#form_register_user').hide();
}

function gotoLogin(){
    $('#form_register_user').hide();
    $('#form_login_user').show();
}

function hide_login(){
    $('#form_login_user').hide();
}

function show_login(){
    $('#form_login_user').show();
}




// FUNCIONS DE USERPANEL
//TO-DO eliminar duplicitat de funció @mfernandez et toca a tu lmao piro al gym
function carregarImatgeAvatar() {
    let input = document.getElementById('inputAvatar');

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#imgAvatar').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}

function carregarImatgeProducte() {

    console.info('dins de');
    let input = document.getElementById('inputImagen');

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#imgProduct').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}


//TO-DO eliminar duplicitat de funció @mfernandez et toca a tu lmao piro al gym
function carregarImatgeAvatar() {
    let input = document.getElementById('inputAvatar');

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#imgAvatar').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}


/* */
function selectProduct(e) {
    
    $('#inputNombre').val(e.children[1].textContent);
    //$('#inputPrice').val(e.children[2].textContent);
    var price = e.children[2].textContent;
    var price_sense_eur = price.substr(0, price.length-2)
    $('#inputPrice').val(price_sense_eur);
    $('#inputDescripcionProd').val(e.children[4].textContent);
    $('#idProduct').val(e.children[5].textContent);

    //console.info($('#inputImagen').val());
    //$('#inputImagen').val(e.children[3].textContent);
    
    $('#imgProduct').attr('src', '/static/img/' + e.children[3].textContent);

    $('#updateOrNew').val('update');
    
}


function emptyProductForm(){

    $('#updateOrNew').val('new');
    $('#inputNombre').val('');
    $('#inputPrice').val('');
    $('#inputDescripcionProd').val('');
    $('#imgProduct').attr('src', '#');
    $('#idProduct').val('');
}

function deleteProduct(){
    
    $('#updateOrNew').val('delete');

    $('#form_productdata')[0].submit();

    emptyProductForm();
}