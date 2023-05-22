import {acceptHMRUpdate, defineStore} from "pinia";
import api from "@/axios";

export const useFileStore = defineStore({
  id: "file",
  state: () => ({
    files: {},
    deleted_files: {},
  }),
  persist: true,
  getters: {

  },
  actions: {
    getFiles() {
      return api.get("/files.json").then((res) => {
        this.files = res.data;
      });
    },
    deleteFile(file_id) {
      return api.delete("/files/" + file_id + "/").then((res) => {
        if (res.status === 204) {
          const index = this.state.files.findIndex(
            (file) => file.id === file_id
          );
          this.state.files.splice(index, 1);
          return true;
        }
      });
    },
    softDeleteFile(file_id) {
      return api.post("/files/" + file_id + "/set_soft_delete/").then((res) => {
        if (res.status === 204) {
          const index = this.state.files.findIndex(
            (file) => file.id === file_id
          );
          this.state.files.splice(index, 1);
          return true;
        }
      });
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useFileStore, import.meta.hot));
}
