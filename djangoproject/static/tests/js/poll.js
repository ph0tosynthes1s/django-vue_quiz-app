new Vue({
    el:'#poll_app',
    data:{
        items:[],
        choose:[],
        radioValue:''

    },
    delimiters: ['[[',']]'],
    created: function () {
        const vm = this;
        const url = window.location.href;
        const path = url.split("/").reverse()[1];
        axios.get(`/api/${path}`)
        .then(function (response){
            data = response.data
            vm.items = data
        })
    },
    methods:{
        check(question_id, option_id, id){
            let radios = document.querySelectorAll(`#radio_${id}`)
            let radiosCheckedCount = 0
            for(let i =0; i < radios.length; i++){
                radios[i].disabled = true;
            }
            const choose = {'question_id': id, 'option':option_id+1}
            this.choose.push(choose)
        },
        handleSubmit(){

            const url = window.location.href;
            const path = url.split("/").reverse()[1];
            console.log(this.choose)
            fetch(`/api/score`, {
                method:'POST',
                headers:{
                    'Accept':'application/json',
                    'Content-type':'application/json'
                },
                body: JSON.stringify({
                    data: JSON.stringify(this.choose),
                    poll_id: path
                })
            })
            .then(res => res.json())
            .then(result => {
                console.log(result)
            })
        }
    }
})