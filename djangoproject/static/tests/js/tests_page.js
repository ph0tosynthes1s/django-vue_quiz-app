new Vue({
    el:'#tests_app',
    data:{
        items:[]
    },
    delimiters: ['[[',']]'],
    created: function () {
        const vm = this;
        axios.get('/api/polls')
        .then(function (response){
            vm.items = response.data
            console.log(response.data)
        })
    }
})