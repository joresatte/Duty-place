<template>
    <div class="modal-backdrop">
        <div class="modal">
            <header class="modal-header">
                <Button icon="pi pi-times" class="danger" text raised rounded aria-label="Cancel" @click="CloseActualModal"/>
                <slot name="header">
                all camps are required!
                </slot>
            </header>
            <section class="modal-body">
            <slot name="body">
                <span class="p-input-icon-left">
                    <i class="pi pi-user" />
                    <InputText v-model="userRequest.name"
                                required 
                                type="text" 
                                size="normal" 
                                placeholder="Please enter your name"
                                @change="onRequested"
                                v-tooltip.bottom="'Enter your email'" 
                                />
                </span><br><br>
                <span class="p-input-icon-left">
                    <i class="pi pi-question-circle" />
                    <InputText v-model="userRequest.subject" 
                                required
                                type="text" 
                                size="normal" 
                                placeholder="Subject"
                                @change="onRequested"
                                v-tooltip.bottom="'Enter your email'" 
                                />
                </span><br><br><br>
                <span class="p-float-label">
                    <Textarea v-model="userRequest.comments"
                              required
                              rows="5" 
                              cols="30" 
                              @change="onRequested"/>
                    <label class="pi pi-comments" > Enter here your comments</label>
                </span>
            </slot>
            </section>
            <footer class="modal-footer">
                <Button type="button" label="Search" severity="help" icon="pi pi-send" :loading="loading" @click="sendRequest" iconPos="right"/>
            <br>
                <Button label=" Cancel " class="danger" rounded @click="CloseActualModal"/>
            </footer>
        </div>
    </div>
</template>
<script>
export default{
    name: 'requestForm',
    emits:['change', 'onChangedRequest', 'onCancelBtnClicked', 'sendRequest'],
    props:{
        userRequest:{
            type: Object,
            required: true,
        }
    },
    data(){
    return{
        loading: false
    }
    },
    methods:{
        onRequested(event){
            console.log('username is: ',event.target.value)
            this.$emit('onChangedRequest', {
            name: event.target.value,
            subject: this.userRequest.subject,
            comments: this.userRequest.comments
          })
        }, 
        onRequested(event){
            console.log('the subject is: ',event.target.value)
            this.$emit('onChangedRequest', {
            name: this.userRequest.name,
            subject: event.target.value,
            comments: this.userRequest.comments
          })
        },
        onRequested(event){
            console.log('the comments are: ',event.target.value)
            this.$emit('onChangedRequest', {
            name: this.userRequest.name,
            subject: this.userRequest.subject,
            comments: event.target.value
          })
        },
        sendRequest(){
            console.log(this.sendRequest)
                this.$emit('sendRequest')
                this.loading= true
            setTimeout(() => {
                this.loading = false;
            }, 2000);
        },
        CloseActualModal(){
            console.log('close modal', this.CloseActualModal)
            this.$emit('onCancelBtnClicked');
        }
    }
}
</script>
<style scoped>
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
        padding: 1.5em;
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
        padding: 2em 2em;
    }
    .danger{
        background-color: red;
    }
</style>