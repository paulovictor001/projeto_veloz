let row_table = document.querySelectorAll('.row_table')
let campo_add_produto = document.getElementById('a')
let campo_vendas = document.getElementById('produtos')
let bt_adicionar = document.querySelectorAll('.botao_adicionar')
let bt_editar = document.querySelectorAll('.bt_editar')
let form_ediçao = document.querySelector('#form_ediçao')
let formulario = document.querySelector('#fomulario_add_produto')

for(let c=0; c<row_table.length;c++){
    row_table[c].addEventListener('click',()=>{

        let focus_bt = document.querySelectorAll('.fip')[c]
        focus_bt.focus()
    })
}
let botao_adicionar_produto = document.querySelector('.bt_adiciona_produto')
botao_adicionar_produto.addEventListener('click',()=>{
    formulario.style.display='block'
})

for (c=0;c<bt_editar.length;c++){
    let input_id = document.querySelector('#id_produto')
    bt_editar[c].addEventListener('click',(avento)=>{
        const id_produto = avento.target.parentNode.parentNode.childNodes[1].innerHTML
        input_id.value=id_produto
        form_ediçao.style.display='block'


    })
}

let bt_sair = document.querySelectorAll('.sair')
for(c=0;c<bt_sair.length;c++){
console.log(bt_sair[c])
    bt_sair[c].addEventListener('click',(evento)=>{
        evento.preventDefault()
        evento.target.parentNode.style.display='none'
    })
}

const bt_deletar = document.querySelectorAll('.bt_deletar')
for (c=0;c<bt_deletar.length;c++){
    
    bt_deletar[c].addEventListener('click',(evento)=>{
        evento.preventDefault()
        
        const msg_delet = document.querySelector('#msg_delet')
        msg_delet.style.display='block'

        const id_produto = evento.target.parentNode.parentNode.childNodes[1].innerHTML
        input_id_produto = document.querySelector('#iid_produto')
        input_id_produto.value = id_produto

    })
}

const bt_cancelar_delet = document.querySelector('#nao_delet')
bt_cancelar_delet.addEventListener('click',(evento)=>{
    evento.preventDefault()
    msg_delet.style.display = 'none'
})
