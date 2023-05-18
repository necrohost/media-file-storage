<template>
  <div class="container-files">
    <div class="table-responsive">
      <table class="table">
        <caption>
          Files
        </caption>
        <thead>
          <tr>
            <th
              v-for="field in fields"
              :key="field"
              scope="col"
              data-sortable="true"
              data-sorter="alphanum"
            >
              {{ field }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="file in this.userFiles"
            :key="file.id"
            style="vertical-align: middle"
            class="file-row"
          >
            <td v-for="field in Object.keys(fields)" :key="field">
              <span v-if="field === 'name'">
                <i
                  :class="withIcon(file)"
                  style="
                    font-size: 30px;
                    margin-right: 15px;
                    color: var(--accent-files-color);
                  "
                ></i>
                <span style="font-size: 15px">{{ file.name }}</span>
              </span>
              <span v-else-if="field === 'upload_at'">
                {{ new Date(file.created_at).toString().slice(0, -32) }}
              </span>
              <span v-else-if="field === 'size'">
                {{ getReadableBytes(file.size) }}
              </span>
              <span v-else-if="field === 'shared_link'">
                <a
                  :href="'http://localhost:8000/api/s/' + file.shared_link"
                  v-if="file.shared_link"
                  ><i icon="fa-solid fa-share-nodes"></i>link</a
                >
              </span>
              <span v-else>{{ file[field] }}</span>
              <!--                file.ext.replace('.', '')-->
            </td>
            <td>
              <div class="dropdown">
                <button
                  class="btn"
                  type="button"
                  id="dropdownMenuButton"
                  data-bs-toggle="dropdown"
                  aria-haspopup="true"
                  aria-expanded="false"
                >
                  <i class="fa-solid fa-ellipsis-vertical"></i>
                </button>
                <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                  <a
                    class="dropdown-item"
                    href="#download"
                    @click="downloadFile(file)"
                    ><i class="fa-solid fa-download"></i> Download</a
                  >
                  <a class="dropdown-item" :href="file.file"
                    ><i class="fa-solid fa-eye"></i> View</a
                  >
                  <a
                    class="dropdown-item"
                    href="#share"
                    @click="shareFile(file)"
                    ><i class="fa-solid fa-share"></i> Share</a
                  >
                  <a class="dropdown-item" href="#"
                    ><i class="fa-solid fa-trash"></i> Delete</a
                  >
                  <a class="dropdown-item" href="#" @click="deleteFile(file)"
                    ><i class="fa-solid fa-square-minus"></i> Permanently
                    delete</a
                  >
                </div>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { collapsed, toggleNav } from "@/components/navbar/state";
import api from "@/axios";
import { useRoute } from "vue-router";
import { useFileStore } from "@/stores/file";

export default {
  name: "Files",
  setup() {
    const file = useFileStore();
    const fields = {
      name: "Name",
      created_at: "Modified",
      size: "Size",
      ext: "Format",
      shared_link: "Share",
    };
    return { file, collapsed, toggleNav, fields };
  },
  data() {
    return {
      userFiles: [],
    };
  },
  computed: {
    route: () => useRoute(),
  },
  methods: {
    getReadableBytes(size) {
      size = Math.round(size / 1024);
      return size <= 1024 ? size + "kb" : Math.round(size / 1024) + "mb";
    },
    withIcon(file) {
      const ext = file.ext.replace(".", "").toLowerCase();
      if (["mp3", "flac"].includes(ext)) {
        return "fa-solid fa-file-audio";
      }
      if (["jpg", "png", "svg"].includes(ext)) {
        return "fa-solid fa-file-image";
      }
      if (["avi", "mp4", "3gp", "mkv"].includes(ext)) {
        return "fa-solid fa-file-video";
      }
      if (["pdf", "doc", "xlsx", "xls"].includes(ext)) {
        return "fa-solid fa-file-lines";
      }
      if (["zip", "rar", "7z", "tar"].includes(ext)) {
        return "fa-solid fa-file-archive";
      }
    },
    downloadFile(file) {
      return api
        .get(`/files/${file.id}/download/`, {
          method: "GET",
          responseType: "blob",
        })
        .then((res) => {
          const url = window.URL.createObjectURL(new Blob([res.data]));
          const link = document.createElement("a");
          link.href = url;
          link.setAttribute("download", file.name);
          document.body.appendChild(link);
          link.click();
        });
    },
    shareFile(file) {
      return api.post(`/files/${file.id}/share/`).then((res) => {
        console.log(res.data);
      });
    },
    deleteFile(file) {
      if (this.file.deleteFile(file.id)) {
        return console.log("deleted file");
      }
    },
  },
  mounted() {
    if (this.route.name === "files") {
      this.userFiles = this.file.files;
    }
    // if (this.route.name === "shared-files") {
    //   this.userFiles = this.file.shared_files;
    // }
    if (this.route.name === "trash") {
      this.userFiles = this.deleted_files;
    }
  },
  created() {
    this.file.getFiles();
  },
};
</script>

<style scoped>
.container-files {
  background-color: #fff;
  margin-bottom: 70px;
  min-height: 100vh;
  padding: 40px;
  border-radius: 0 5px 5px 0;
  /*-webkit-box-shadow: -4px -4px 15px 4px rgba(0, 0, 0, 0.1);*/
  //-moz-box-shadow: -4px -4px 15px 4px rgba(0, 0, 0, 0.1); //box-shadow: -4px -4px 15px 4px rgba(0, 0, 0, 0.1); box-shadow: 0 0 2px rgba(58, 66, 75, 0.1), 0 2px 4px rgba(58, 66, 75, 0.2);
}

.table-responsive {
  min-height: 100vh;
}
</style>
