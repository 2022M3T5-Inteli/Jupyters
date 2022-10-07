$(".type").click(function () {
    var button_text = $(this).text();
    if(button_text === 'Rat') {
        $('#rat-tb').show()
        $('#rch-tb').hide()
        $('#shr-tb').hide()
    }
    if(button_text === 'Shr') {
        $('#rat-tb').hide()
        $('#rch-tb').hide()
        $('#shr-tb').show()
    }
    if(button_text === 'Rch') {
        $('#rat-tb').hide()
        $('#rch-tb').show()
        $('#shr-tb').hide()
    }
})

function generateTable(data) {
    const rat = $('#table-rat')
    const shr = $('#table-shr')
    const rch = $('#table-rch')
    let rat_html = ''
    let rch_html = ''
    let shr_html = ''
    Object.keys(data['demographic_rats']).forEach(key => {
        if (key !== 'Total Domicílios | Rat%') {
            rat_html +=
                `<tr>
                <th scope="row">${key}</th>
                <td>${data['demographic_rats'][key].toFixed(2)}</td>
              </tr>`
            
        }

    })
    rat.html(rat_html)
    Object.keys(data['shr']).forEach(key => {
        shr_html +=
            `<tr>
                <th scope="row">${key}</th>
                <td>${data['shr'][key].toFixed(2)}</td>
              </tr>`
        
    })
    shr.html(shr_html)
    Object.keys(data['rch']).forEach(key => {
        rch_html +=
            `<tr>
                <th scope="row">${key}</th>
                <td>${data['rch'][key].toFixed(2)}</td>
              </tr>`
        
    })
    rch.html(rch_html)
}

const data = {
    labels: [],
    datasets: [{
        backgroundColor: 'rgb(255, 99, 132)',
        borderColor: 'rgb(255, 99, 132)',
        data: [],
    }]
};

const config = {
    type: 'line',
    data: data,
    options: {
        plugins: {
            legend: {
                display: false
            }
        }
    }
};

myChart = new Chart(
    document.getElementById('plot'),
    config
);

function show_graph(data) {
    myChart.data.labels = data['time_array']
    myChart.data.datasets[0].data = data['all_rats']
    myChart.update()
}

$("#enviar").click(function () {
    requestData = {
        "Dia da Semana": Number.parseInt($("#diaSemana").val()),
        "Mês": Number.parseInt($("#mes").val()),
        "Dia": Number.parseInt($("#diaMes").val()),
        "Hora": Number.parseInt($("#hora").val()),
        "Minuto": Number.parseInt($("#minuto").val()),
        "Feriado": 0,
        "Categoria_AUDITORIO": 0,
        "Categoria_CARROS E MOTORES": 0,
        "Categoria_CULINARIO": 0,
        "Categoria_DEBATE": 0,
        "Categoria_DOCUMENTARIO": 0,
        "Categoria_EDUCATIVO": 0,
        "Categoria_ENTREVISTA": 0,
        "Categoria_ESPORTE": 0,
        "Categoria_FEMININO": 0,
        "Categoria_FILME": 0,
        "Categoria_FUTEBOL": 0,
        "Categoria_GAME SHOW": 0,
        "Categoria_HUMORISTICO": 0,
        "Categoria_JORNALISMO": 0,
        "Categoria_MINISSERIE": 0,
        "Categoria_MUSICAL": 0,
        "Categoria_NOVELA": 0,
        "Categoria_POLITICO": 0,
        "Categoria_PREMIACAO": 0,
        "Categoria_REALITY SHOW": 0,
        "Categoria_RELIGIOSO": 0,
        "Categoria_REPORTAGEM": 0,
        "Categoria_RURAL": 0,
        "Categoria_SERIES": 0,
        "Categoria_SHOW": 0,
        "Duração": Number.parseInt($("#duracao").val())
    }

    if ($('#feriado').is(":checked")) {
        requestData['Feriado'] = 1
    }

    requestData[$('#categoria').val()] = 1
    console.log(requestData)
    $.ajax({
        type: 'post',
        url: 'http://127.0.0.1:5000/predict',
        data: JSON.stringify(requestData),
        contentType: "application/json; charset=utf-8",
        traditional: true,
        success: function (data) {
            $('#result').text(data['main_rat'])
            show_graph(data)
            console.log(data)
            generateTable(data)
        }
    });

});
