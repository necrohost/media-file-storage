<template>
  <div class="upload-container">
    <label class="custom-file-upload">
      <input
        type="file"
        name="file"
        ref="fileInput"
        @change="uploadFile"
        class="my"
      />
      <i class="fa-solid fa-arrow-up-from-bracket"></i>
      <span v-if="!collapsed">Upload</span>
    </label>
    <div v-if="showProgressBar">
      <div class="progress-container">
        <div
          class="progress-bar"
          :style="{ width: uploadProgress + '%' }"
        ></div>
      </div>
      <!--                <span class="progress-text">{{ uploadProgress }}%</span>-->
    </div>
  </div>
</template>

<script>
import axios from "@/axios";
import { collapsed } from "./state";
import { useRoute } from "vue-router";
import { computed } from "vue";
export default {
  setup() {
    return { collapsed };
  },
  data() {
    return {
      showProgressBar: false,
      uploadProgress: 0,
    };
  },
  methods: {
    uploadFile() {
      const file = this.$refs.fileInput.files[0];
      const formData = new FormData();
      formData.append("file", file);
      this.showProgressBar = true;
      axios
        .post("/files/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
          onUploadProgress: (progressEvent) => {
            this.uploadProgress = Math.round(
              (progressEvent.loaded * 100) / progressEvent.total
            );
          },
        })
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<style scoped>
.upload-container {
  width: 100%;
  margin-bottom: 20px;
}

.my {
  position: absolute;
  display: none;
  top: 0;
  left: 0;
  opacity: 0;
  cursor: pointer;
}
.upload-container span {
    margin-left: 5px;
}
.custom-file-upload {
  display: inline-block;
  cursor: pointer;
  border: 1px solid white;
  color: white;
  text-align: center;
  width: 97%;
  padding: 6px;
  text-transform: uppercase;
}
.custom-file-upload:hover {
  color: black;
  background-color: white;
  border-radius: 3px;
  transition: 0.2s ease;
  box-shadow: 0 0 1px 0 white inset, 0 0 1px 0 white;
}

.custom-file-upload:active {
  color: black;
  background-color: white;
}

.progress-container {
  position: relative;
  height: 2px;
  background-color: black;
  /*overflow: hidden;*/
}

.progress-bar {
  height: 2px;
  background-color: white;
  transition: width 0.3s;
}
</style>
