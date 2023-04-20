<template>
  <div class="container-files">
    <div>
      <table id="tableComponent" class="table table-bordered table-striped">
        <thead>
          <tr>
            <!-- loop through each value of the fields to get the table header -->
            <th v-for="field in fields" :key="field">
              {{ field }}
              <i class="fas fa-sort"></i>
            </th>
          </tr>
        </thead>
        <tbody>
          <!-- Loop through the list get the each student data -->
          <tr v-for="file in userFiles" :key="file">
            <td v-for="field in fields" :key="field">{{ file[field] }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import api from "@/axios";
import { collapsed, toggleNav } from "@/components/navbar/state";
import { mapActions, mapState } from "vuex";
export default {
  name: "FilesPage",
  setup() {
    const fields = ["name", "upload_at", "size", "ext", "file"];
    return { collapsed, toggleNav, fields };
  },
  data() {
    return {
      info: null,
      userFiles: {},
    };
  },
  computed: {
    ...mapState(["files"]),
  },
  methods: {
    ...mapActions(["getFiles"]),
  },
  created() {
    this.getFiles().catch((e) => {
      this.$notify({
        type: "error",
        title: "Could not get files, try again later",
        text: e.message ? e.message : null,
      });
    });
  },
  mounted() {
    this.userFiles = this.files;
  },
};
</script>

<style scoped>
h1 {
  color: #fff;
}
</style>
