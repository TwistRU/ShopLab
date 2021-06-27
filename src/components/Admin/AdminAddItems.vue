<template>
  <div>
    <label> Name
      <input
          type="text"
          id="inpName"
          v-model="name"
      >
    </label>
    <label> Price
      <input
          type="text"
          id="inpPrice"
          v-model="price"
      >
    </label>
    <label> Available
      <input
          type="text"
          id="inpAvailable"
          v-model="available"
      >
    </label>
    <label> Rating
      <input
          type="text"
          id="inpRating"
          v-model="rating"
      >
    </label>
    <label> File
      <input
          type="file"
          id="inpImage"
          @change="handleFileUpload"
          ref="image"
          accept="image/*"
      >
    </label>
    <button @click="mySubmit">Send</button>
  </div>
</template>

<script>
import axios from "axios";
import {mapGetters} from "vuex";
import {host} from "@/main";

export default {
  name: "AdminAddItems",
  data() {
    return {
      image: '',
      name: '',
      price: '',
      available: '',
      rating: '',
    }
  },
  methods: {

    mySubmit() {
      return axios({
        method: 'POST',
        url: host + '/api/v1/item',
        data: {
          image: this.image,
          name: this.name,
          price: Number(this.price),
          available: Number(this.available),
          rating: Number(this.rating),
        },
        headers: {
          "Authorization": "Bearer " + this.CURRENT_ACCESS_TOKEN,
        },
      }).then((response) => {
        console.log("successful")
        return response
      }).catch((response) => {
        console.log(response.error)
        return response
      })
    },

    handleFileUpload() {
      let reader = new FileReader();
      reader.onload = (ev) => {
        this.image = ev.target.result;
      }
      reader.readAsDataURL(this.$refs.image.files[0]);
    },
  },
  computed: {
    ...mapGetters([
      'CURRENT_ACCESS_TOKEN',
    ]),
  }
}
</script>

<style scoped>

</style>