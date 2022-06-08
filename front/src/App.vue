<template>
 <Toolbar style="height: 6em;" class="toolbar">
  <template #start>
    <nav><headerNav/></nav><br><br>
    <div style="margin-top: 2em; margin-left: 0;">
    <Button icon="pi pi-arrow-right" @click="visibleLeft = true" class="mt-6" />
    <Sidebar v-model:visible="visibleLeft" style="background-color: #B7E9F3;">
    <h3>DashBord</h3>
    <Menu :model="items" />
    </Sidebar>
    </div>
  </template>
</Toolbar>
<div class="header_nav">
</div>
<span class="btn-logout">
  <Button
      class="p-button-outlined p-button-success"
      style="color:aliceblue;"
      type="button"
      label="Sign Out"
      icon="pi pi-sign-out" iconPos="right"
      @click.prevent="handleLogout"
      :disabled="isLoggedOut"
      v-if="LoggedOut"
    >
  </Button>
</span>
<div id="app">
    <span class="btn-regist">
      <Button
        style="color:aliceblue;"
        class="p-button-outlined p-button-success p-xl-none"
        type="button"
        label="Sign Up"
        icon="pi pi-sign-in" iconPos="left"
        @click="clickedToSwitchOnModal"
        v-if="SignUp"
      >
      </Button>
    </span>
    <span class="btn-login">
      <Button
        style="color:aliceblue;"
        class="p-button-outlined p-button-success"
        type="button"
        label="Log In"
        icon="pi pi-sign-in" iconPos="right"
        @click="onModalOnclicked"
        v-if="LogIn"
      >
      </Button>
    </span>
    <button  @click="clickedToSwitchOffModal" v-if="showRegist">
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
      <span><Button label="CREATE ACCOUNT" icon="pi pi-check" @click="ClickToRegist"> </Button></span>
      <footer class="modal-footer">
        <slot name="footer">
          <br>
        <span><Button label="close Modal" class="p-button-link" icon="pi pi-times" @click="closeRegistModal"></Button></span>
        </slot>
        
      </footer>
    </div>
  </div>
      </button>
  </div>
    <button  @click="offModalOnclicked" v-if="showLogin">
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
      <span ><Button label="Log In" icon="pi pi-sign-in"  @click="ClickToLogIn"></Button></span>
      <footer class="modal-footer">
        <slot name="footer">
          <br>
          <span><Button class="p-button-link" icon="pi pi-times" label="close modal" @click="closeLoginModal"></Button></span>
        </slot>
        
      </footer>
    </div>
  </div>
      </button>
  <section v-show="error">invalid Log In </section>
  <router-view/>
</template>
<script>
// import axios from 'axios';
// import config from "@/config.js";
import emailForm from '@/components/RegistEmailForm.vue'
import passwordForm from '@/components/RegistPasswordForm.vue';
import LoginEmail from '@/components/LoginEmailForm.vue'
import LoginPassword from '@/components/LoginPasswordForm.vue';
import getRegistPost from '@/pages/apiservices/getRegistPost.js'
import getLoginPost from '@/pages/apiservices/getLoginPost.js'
import headerNav from '@/components/headerNavForm.vue'
import getCurrentUser from '@/pages/apiservices/getCurrentUser.js'
import Swal from 'sweetalert2'
export default {
  name: 'app',
  components:{emailForm, passwordForm, headerNav, LoginEmail, LoginPassword},
  data(){
    return{
      reset:false,
      email:'',
      password: '',
      showRegist: false,
      showLogin: false,
      LogIn:true,
      SignUp: true,
      LoggedOut: false,
      userId: {},
      error: false,
      visibleLeft: false,
      items:[
        {
          label: 'Options',
           items:[
             {
               label: 'Update',
                        icon: 'pi pi-refresh',
             },
             {
               label: 'Sign Up',
                        icon: 'pi pi-sign-in',
                        command: ()=>{
                          if(window.localStorage){
                            if(
                              localStorage.getItem('dataUser')!== undefined && localStorage.getItem('dataUser')
                              ){
                              this.showRegist= false
                            }else{
                            this.showRegist= true
                            
                            }
                          }
                        }
             },
             {
               label: 'Login In',
                        icon: 'pi pi-sign-in',
                        command: ()=>{
                          if(window.localStorage){
                            if(
                              localStorage.getItem('dataUser')!== undefined && localStorage.getItem('dataUser')
                              ){
                              this.showLogin= false
                            }else{
                            this.showLogin= true
                            
                            }
                          }
                        }
             },
             {
               label: 'Publish Service',
                        icon: 'pi pi-save',
                        command: ()=>{
                          if(window.localStorage){
                            if(
                              localStorage.getItem('dataUser')!== undefined && localStorage.getItem('dataUser')
                              ){
                              this.$router.push({
                                 path: '/user_services/:id',
                                 name: 'publishServicePage',
                                 params:{id: getCurrentUser()}
                              })
                            }else{
                            alert('you must log in first')
                            }
                          }
                        }
             },
           ]
        }
      ],
    }
  },
  mounted(){
    if(window.localStorage){
     if(localStorage.getItem('dataUser')!== undefined && localStorage.getItem('dataUser') ){
       return this.getLoggedOut()
     }else{
       return this.getBackToHome()
     }
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
    async ClickToRegist (){
      console.log(this.ClickToRegist)
      const re_email= "[a-zA-Z0-9!#$%&'*_+-]([\.]?[a-zA-Z0-9!#$%&'*_+-])+@[a-zA-Z0-9]([^@&%$\/()=?¿!.,:;]|\d)+[a-zA-Z0-9][\.][a-zA-Z]{2,4}([\.][a-zA-Z]{2})?"

      if (
        this.email!='' && re_email.match( this.email) || 
        this.password!='' && this.password.lenghth >=7){
        await getRegistPost()
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
        }
        this.email= '';
        this.password='';
      },
      onModalOnclicked(){
        this.showLogin = true
         if (this.showLogin==true){
          this.showRegist= false
        }
      },
      clickedToSwitchOnModal(){
        this.showRegist = true
        if (this.showRegist==true){
          this.showLogin= false
        }
      },
      closeLoginModal(){
        this.showLogin= false
      },
      closeRegistModal(){
        this.showRegist= false
      },
      getUserId() {
      const userJson = localStorage.getItem("dataUser");
      const user = JSON.parse(userJson);
      return user.id;
      },
      getLoggedOut(){
          this.SignUp= false
          this.LogIn= false
          this.showLogin= false
          this.LoggedOut= true
      },
      getBackToHome(){
        this.SignUp= true
        this.LogIn= true
        this.LoggedOut= false
        this.$router.push({
                            path: '/',
                            name: 'Home',
                          })
      },
      handleLogout(){
        localStorage.clear('dataUser')
       this.getBackToHome()
      },
      async ClickToLogIn(){
         if (this.email!='' || this.password!=''){
           const response= await getLoginPost(this.email, this.password)
           console.log('login', this.ClickToLogIn )
           const loginStatusCode = response.status
           console.log('response', loginStatusCode)
            if(loginStatusCode== 401){
               Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'invalid login!',
                footer: '<a href="http://localhost:8080/">the email and password fields are required</a>'
              })
            }else{
                this.userId= await response.json()
                console.log(this.userId)
                localStorage.setItem('dataUser', JSON.stringify(this.userId))
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
              text: 'all camps are required!',
              footer: '<a href="http://localhost:8080/">the email and password fields are required</a>'
            })
          } 
          this.email= '';
          this.password='';
      }, 
  }
}
</script>
<style lang="stylus">
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
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
  height: 1em
}
.sideBar{
  background: linear-gradient(90deg, 
              rgba(10,10,142,0.33703903924851186) 22%, 
              rgba(8,17,37,1) 49%, 
              rgba(2,2,11,0.33703903924851186) 77%);
}
.btn-logout{
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
 position: absolute;
 top: 0;
 right: 7em;
 color: white;
 font-size: 1em;
 border-radius: 2px;
 text-decoration: none;
 padding: 0.2em;
}
.btn-login{
  position: absolute;
  top: 0;
  right: 0;
  color: white;
  font-size: 1em;
  border-radius: 2px;
  text-decoration: none;
  padding: 0.2em;
}
.btn-remove{
  margin-left: 3.5em 
  background: linear-gradient(90deg, rgba(4,15,38,1) 0%,
              rgba(11,11,157,0.33703903924851186) 28%,
              rgba(26,47,51,0.8076272745426296) 55%);
  position: relative;
  top: auto;
  right: auto;
  width: 8em
  color: white;
  font-size: 1em;
  border-radius: 2px;
  text-decoration: none;
  padding: 0.2em;
}
.toolbar{
  background: linear-gradient(90deg, rgba(4,15,38,1) 0%,
            rgba(11,11,157,0.33703903924851186) 28%,
            rgba(26,47,51,0.8076272745426296) 55%);
}
.btn-edit{ 
  background: linear-gradient(90deg, rgba(4,15,38,1) 0%,
              rgba(11,11,157,0.33703903924851186) 28%,
              rgba(26,47,51,0.8076272745426296) 55%);
  position: relative;
  top: auto;
  right: auto;
  width: 8em
  color: white;
  font-size: 1em;
  border-radius: 2px;
  text-decoration: none;
  padding: 0.2em;
}
.edit_remove{
  display: flex
  flex-flow: nowrap
  justify-content: space-between
  margin-top: 3em;
  align-items: center;
}
.page{
  margin: 0.5em;
  font-size: 2em;
  color: #2fa8ba;
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
  background: linear-gradient(90deg, rgba(4,15,38,1) 0%,
              rgba(11,11,157,0.33703903924851186) 28%,
              rgba(26,47,51,0.8076272745426296) 55%);
  border: 1px solid #4AAE9B;
  border-radius: 2px;
}
.btn-handleEditClick {
  color: white;
  background: #4AAE9B;
  border: 1px solid #4AAE9B;
  border-radius: 2px;
  height: 2em
}
#filtered_category{
  height: 2em;
  position: relative;
  top: -6em;
}
#filtered_option{
  height: 2em;
  position: relative;
  top: -5em;
}
.user-profile{
  display: flex;
  flex-direction: flex start;
}
.image_category{
  width:65%;
  border-radius: 5px;
}
.user-info{
  margin-left: -1em;
}
</style>
