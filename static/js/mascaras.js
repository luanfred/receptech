
var options = {
    onKeyPress: function (cpf, ev, el, op) {
        var masks = ['000.000.000-000', '00.000.000/0000-00'];
        $('.cpfcnpj').mask((cpf.length > 14) ? masks[1] : masks[0], op);
    }
}

$('.cpfcnpj').length > 11 ? $('.cpfcnpj').mask('00.000.000/0000-00', options) : $('.cpfcnpj').mask('000.000.000-00#', options);

$('.telefone').on('input', function () {
    let tamanho = $(this).val().length;
    if (tamanho < 14) {
        $(this).mask('(00) 0000-0000');
    } else {
        $(this).mask('(00) 00000-0000');
    }
})

$('.cep').mask('00000-000');

$('.numerico').on('input', function () {
    $(this).mask('000.000.000', { reverse: true });
})

$('.numerico_2').on('input', function () {
    $(this).mask('000.000,00', { reverse: true });
})

$('.decimal').on('input', function () {
    $(this).val($(this).val().replace(/[^0-9.]/g, ''));
})
