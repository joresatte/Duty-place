<template>
<br>
<nav>
<headerNav/>
</nav>
<div class="header_nav">
</div>
<div id="app">
    <button
      type="button"
      class="btn-regist"
      @click="clickedToSwitchOnModal"
    >
      Sign up
    </button>
    <button  @click="clickedToSwitchOffModal" v-show="showRegist">
        <div class="modal-backdrop">
    <div class="modal">
      <header class="modal-header">
        <slot name="header">
          feel all camps to regist
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
          close Modal
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
    >
      login
    </button>
    <button  @click="offModalOnclicked" v-show="showLogin">
        <div class="modal-backdrop">
    <div class="modal">
      <header class="modal-header">
        <slot name="header">
          feel all camps to log in
        </slot>
      </header>

      <section class="modal-body">
       <emailForm :newEmail="email" @onEmailChanged="onChangedEmail"/>
       </section>
       <section class="modal-body">
        <passwordForm :newPassword="password" @onPasswordChanged="onChangedPassword"/>
       </section>
      <button class="btn-regist-login" @click="ClickToLogIn">Log in</button>
      <footer class="modal-footer">
        <slot name="footer">
          <br>
          close Modal
        </slot>
        
      </footer>
    </div>
  </div>
      </button>
  </div>
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
          this.email = event
          JSON.stringify(localStorage.setItem('registEmail', event))
      },
    onChangedPassword(newPassword){
          console.log(newPassword )
          this.password= newPassword
          JSON.stringify(localStorage.setItem('registPassword', newPassword))
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
        alert('sign up successfully')
        this.$forceUpdate()
         this.$router.push({
                            path: '/',
                            name: 'Home',
                          })
      }else{
        alert('the email and password fields are required')
      }
      },
      onModalOnclicked(){this.showLogin = true},
      offModalOnclicked(){this.showLogin = false},
      clickedToSwitchOnModal(){this.showRegist = true},
      clickedToSwitchOffModal(){this.showRegist = false},
      async ClickToLogIn(){
        if (this.email!='' || this.password!=''){
        await getLoginPost()
        console.log(getLoginPost)
        const loginStatusCode= response.status

        if(loginStatusCode== 403){
           alert('invalid login')
        }else{
          const user= localStorage.setItem('user', await response.json())
          alert('log in successfully')
          console.log(user)
          this.$router.push({
             path: '/user',
             name: 'usersPage',
          })
        }
      }else{
        alert('the email and password fields are required')
      } 
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

.btn-green {
  color: white;
  background: #4AAE9B;
  border: 1px solid #4AAE9B;
  border-radius: 2px;
}
</style>
