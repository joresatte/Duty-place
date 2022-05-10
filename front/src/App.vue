<template>
<br>
<nav>
<headerNav/>
</nav>
<div class="header_nav">
</div>

<button
    class="btn-logout"
    @click.prevent="handleLogout"
    :disabled="isLoggedOut"
    v-if="LoggedOut"
  >
    Log out
</button>

<div id="app">
    <button
      type="button"
      class="btn-regist"
      @click="clickedToSwitchOnModal"
      v-if="SignUp"
    >
      Sign Up
    </button>
    <button  @click="clickedToSwitchOffModal" v-show="showRegist">
        <div class="modal-backdrop">
    <div class="modal">
      <header class="modal-header">
        <slot name="header">
          feel all camps to Regist
        </slot>
      </header>

      <section class="modal-body">
       <emailForm :newEmail="email" @onEmailChanged="onChangedEmail"/>
       </section>
       <section class="modal-body">
        <passwordForm :newPassword="password" @onPasswordChanged="onChangedPassword"/>
       </section>
      <button class="btn-regist-login" @click="ClickToRegist"> CREATE ACCOUNT</button>
      <footer class="modal-footer">
        <slot name="footer">
          <br>
        <button @click="closeRegistModal">close Modal</button>
        </slot>
        
      </footer>
    </div>
  </div>
      </button>
  </div>


 <div id="app">
    <button
      type="button"
      class="btn-login"
      @click="onModalOnclicked"
      v-if="LogIn"
    >
      Log In
    </button>
    <button  @click="offModalOnclicked" v-show="showLogin">
        <div class="modal-backdrop">
    <div class="modal">
      <header class="modal-header">
        <slot name="header">
          feel all camps to Log In
        </slot>
      </header>

      <section class="modal-body">
       <LoginEmail :renewEmail="email" @EmailChanged="onEmailChanged"/>
       </section>
       <section class="modal-body">
        <LoginPassword :renewPassword="password" @ChangedPassword="onPasswordChanged"/>
       </section>
      <button class="btn-regist-login" @click="ClickToLogIn">Log In</button>
      <footer class="modal-footer">
        <slot name="footer">
          <br>
          <button @click="closeLoginModal">close Modal</button>
        </slot>
        
      </footer>
    </div>
  </div>
      </button>
  </div>
  <router-view/>
</template>
<script>
// import axios from 'axios';
// import config from "@/config.js";
import getCurrentUser from '@/pages/apiservices/getCurrentUser.js'
import emailForm from '@/components/RegistEmailForm.vue'
import passwordForm from '@/components/RegistPasswordForm.vue';
import LoginEmail from '@/components/LoginEmailForm.vue'
import LoginPassword from '@/components/LoginPasswordForm.vue';
import getRegistPost from '@/pages/apiservices/getRegistPost.js'
import getLoginPost from '@/pages/apiservices/getLoginPost.js'
import headerNav from '@/components/headerNavForm.vue'
import Swal from 'sweetalert2'
export default {
  name: 'app',
  components:{emailForm, passwordForm, headerNav, LoginEmail, LoginPassword},
  data(){
    return{
      currentUser: getCurrentUser(),
      email:'',
      password: '',
      showRegist: false,
      showLogin: false,
      LogIn:true,
      SignUp: true,
      LoggedOut: false,
      userId: [],
    }
  },
  mounted(){
    if(this.currentUser){
      return this.getLoggedOut()
    }
  },
  computed: {
  isLoggedOut() {
    return ;
  },
},
  methods:{
    onChangedEmail(event){
          console.log(event)
          this.email = event
          JSON.stringify(localStorage.setItem('registEmail', event))
      },
    onChangedPassword(newPassword){
          console.log(newPassword )
          this.password= newPassword
          JSON.stringify(localStorage.setItem('registPassword', newPassword))
      },
    onEmailChanged(newEvent){
          console.log(newEvent)
          this.email = newEvent
          JSON.stringify(localStorage.setItem('loginEmail', newEvent))
      },
    onPasswordChanged(PasswordValue){
          console.log(PasswordValue )
          this.password= PasswordValue
          JSON.stringify(localStorage.setItem('loginPassword', PasswordValue))
      },
      // isValid(){
      //   console.log('es valido?', this.isValid)
      //   if(
      //     this.email || this.password!==''
      //   ){
      //     return true
      //   }else{
      //     return false
      //   }
      // },
    async ClickToRegist (){
      console.log(this.ClickToRegist)
      if (this.email!='' || this.password!=''){
        await getRegistPost()
        // alert('saved successfully')
        Swal.fire(
          'success',
          'Sign Up successfully',
          'Saved'
        )
         this.$router.push({
                            path: '/',
                            name: 'Home',
                          })
         this.showRegist= false
      }else{
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: 'Something went wrong!',
          footer: '<a href="http://localhost:8080/">the email and password fields are required</a>'
        })
        this.email= '';
        this.password='';
      }
      },
      onModalOnclicked(){this.showLogin = true},
      // offModalOnclicked(){this.showLogin = false},

      clickedToSwitchOnModal(){this.showRegist = true},
      // clickedToSwitchOffModal(){this.showRegist = false},
      closeLoginModal(){
        this.showLogin= false
      //   this.$router.go({
      //    path: '/',
      //    name: 'Home',
      // })
      },
      closeRegistModal(){
        this.showRegist= false
      //   this.$router.go({
      //    path: '/',
      //    name: 'Home',
      // })
      },
      getUserId() {
      const userJson = localStorage.getItem("dataUser");
      const user = JSON.parse(userJson);
      return user.id;
      },
      getLoggedOut(){
          this.SignUp= false
          this.LogIn= false
          this.LoggedOut= true
          this.showLogin= false
      },
      handleLogout(){
        localStorage.removeItem('dataUser')
        this.$router.push({
           path: '/',
           name: 'Home',
        })
        this.SignUp= true
        this.LogIn= true
        this.LoggedOut= false
      },
      async ClickToLogIn(){
        if (this.email!='' || this.password!=''){
          this.userId= await getLoginPost(this.email, this.password)
          localStorage.setItem('dataUser', JSON.stringify(this.userId))
          const loginStatusCode= this.getUserId()
          console.log(loginStatusCode)

          if(loginStatusCode!= this.getUserId()){
            // alert('invalid login')
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'invalid login!',
              footer: '<a href="http://localhost:8080/">the email and password fields are required</a>'
            })
          }else{
            this.$router.push({
              name: 'usersPage',
              params:{id: this.userId},
              })
              this.getLoggedOut()

            }
          }else{
            // alert('the email and password fields are required')
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Something went wrong!',
              footer: '<a href="http://localhost:8080/">the email and password fields are required</a>'
            })
          } 
          this.email= '';
          this.password='';
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
.btn-logout{
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
.modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }
.modal {
  background: #FFFFFF;
  box-shadow: 2px 2px 20px 1px;
  overflow-x: auto;
  display: flex;
  flex-direction: column;
}
.modal-header,
.modal-footer {
  padding: 15px;
  display: flex;
}

.modal-header {
  position: relative;
  border-bottom: 1px solid #eeeeee;
  color: #4AAE9B;
  justify-content: space-between;
}

.modal-footer {
  border-top: 1px solid #eeeeee;
  flex-direction: column;
  justify-content: flex-end;
}

.modal-body {
  position: relative;
  padding: 20px 10px;
}

.btn-regist-login {
  border: 1px solid #4AAE9B;
  font-size: 1.5em;
  padding: 0.5em;
  cursor: pointer;
  font-weight: bold;
  color: #4AAE9B;
  background: transparent;
}
.btn-regist-login:hover{
  color: blue
}
.btn-green {
  color: white;
  background: #4AAE9B;
  border: 1px solid #4AAE9B;
  border-radius: 2px;
}
</style>
