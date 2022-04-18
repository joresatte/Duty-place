<template>
  <div class="container">
  <div class="box">
    <img src="https://source.unsplash.com/1000x800">
  </div>
  <div class="box">
    <img src="https://source.unsplash.com/1000x802">
  </div>
  <div class="box">
    <img src="https://source.unsplash.com/1000x804">
  </div>
  <div class="box">
    <img src="https://source.unsplash.com/1000x806">
  </div>
</div>
</template>

<script>
export default {
    name: 'imageForm',
}
</script>

<style scoped>
.container {
  display: flex;
  width: 100%;
  padding: 4% 2%;
  box-sizing: border-box;
  height: 50vh;
}

.box {
  flex: 1;
  overflow: hidden;
  transition: .5s;
  margin: 0 2%;
  box-shadow: 0 20px 30px rgba(0,0,0,.1);
  line-height: 0;
}

.box > img {
  width: 200%;
  height: calc(100% - 5vh);
  object-fit: cover; 
  transition: .5s;
}

.box:hover { flex: 1 1 30%; }
.box:hover {
  width: 100%;
  height: 100%;
}
 
</style>