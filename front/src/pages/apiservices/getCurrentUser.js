function getCurrentUser(){
    const userJson = localStorage.getItem("dataUser");
    const user = JSON.parse(userJson);
    return user.id;
}
export default getCurrentUser