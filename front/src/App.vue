<template>
<br>
<nav>
<headerNav/>
</nav>
<div class="header_nav">
</div>
<button @click="onBtnCliked" class="btn-regist"> Sign up
    <section v-show="showRegist" class="show-regist">
       <emailForm :newEmail="email" @onEmailChanged="onChangedEmail"/>
        <passwordForm :newPassword="password" @onPasswordChanged="onChangedPassword($event)"/>
      <button @click="ClickToRegist">CREATE ACCOUNT</button>
      </section>
  </button>
  <button @click="BtnCliked" class="btn-login"> Log in
    <section v-show="showLogin" class="show-login">
       <emailForm :newEmail="email" @onEmailChanged="onChangedEmail($event)"/>
        <passwordForm :newPassword="password" @onPasswordChanged="onChangedPassword($event)"/>
      <button @click="ClickToLogIn">Log in</button>
      </section>
  </button>
  <router-view/>
</template>
<script>
import emailForm from '@/components/emailForm.vue'
import passwordForm from '@/components/passwordForm.vue';
import getRegistPost from '@/pages/apiservices/getRegistPost.js'
import getLoginPost from '@/pages/apiservices/getLoginPost.js'
import headerNav from '@/components/headerNavForm.vue'
export default {
  name: 'app',
  components:{emailForm, passwordForm, headerNav},
  data(){
    return{
      email:'',
      password: '',
      showRegist: false,
      showLogin: false,
    }
  },
  methods:{
    onChangedEmail(event){
            console.log(event)
            // email.value = event
      },
    onChangedPassword(newPassword){
          console.log(newPassword )
          //  password.value= newPassword
      },
      isValid(){
        console.log('es valido', this.isValid)
        if(
          this.email || this.password !=''
        ){
          return true
        }else{
          return false
        }
      },
    async ClickToRegist (){
      if (this.isValid()== true){
        await getRegistPost()
        console.log(getRegistPost)
        alert('sign up successfully')
      }else{
        alert('the email and password fields are required')
       
      }
      this.email='';
      this.password= '';
      this.$router.push('/')
      },
      onBtnCliked(){
        this.showRegist= true
      },
      BtnCliked(){
        this.showLogin= true
      },
      async ClickToLogIn(){
        if (this.isValid()== true){
        await getLoginPost()
        console.log(getLoginPost)
        const loginStatusCode= response.status

        if(loginStatusCode== 403){
           alert('invalid login')
        }else{
          const user= localStorage.setItem('user', await response.json())
          Json.strignyfy(user)
        alert('log in successfully')
        console.log(user)
        }
      }else{
        alert('the email and password fields are required')
      }
        this.password=''
        this.email= '';
        this.$router.push('/')
      }
  }
}
</script>
<style lang="stylus">
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  
}
img {
  width: 100%
  
}
#app
  font-family Avenir, Helvetica, Arial, sans-serif
  -webkit-font-smoothing antialiased
  -moz-osx-font-smoothing grayscale
  text-align center
  color #2c3e50

  *#app
  background white
  
  .header_nav{
  color:white;
  background: linear-gradient(90deg, 
              rgba(10,10,142,0.33703903924851186) 22%, 
              rgba(8,17,37,1) 49%, 
              rgba(2,2,11,0.33703903924851186) 77%);
  font-size:2em;
  padding:10px;
  text-shadow:3px 3px 3px yellow;
  margin-top: 2em;
}
.btn-regist{
background: linear-gradient(90deg, rgba(8,17,37,1) 0%, 
            rgba(10,10,142,0.33703903924851186) 59%, 
            rgba(3,3,25,0.33703903924851186) 79%);
 position: absolute;
 top: 0;
 right: 4em;
 color: white;
 font-size: 1em;
 border-radius: 2px;
 text-decoration: none;
 padding: 0.2em;
}
.btn-login{
background: linear-gradient(90deg, rgba(4,15,38,1) 0%,
            rgba(11,11,157,0.33703903924851186) 28%,
            rgba(26,47,51,0.8076272745426296) 55%);
 position: absolute;
 top: 0;
 right: 0;
 color: white;
 font-size: 1em;
 border-radius: 2px;
 text-decoration: none;
 padding: 0.2em;
}
.page{
  margin: 0.5em;
  font-size: 2em;
  color: #53d9ed;
  text-shadow:  2px 2px 4px #f10889;
}
</style>
