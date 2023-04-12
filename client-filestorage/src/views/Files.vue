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
import axios from "axios";
import { collapsed, toggleNav } from "@/components/navbar/state";
export default {
  name: "FilesPage",
  setup() {
    const fields = [ 'name','upload_at', 'size', 'file' ]
    return { collapsed, toggleNav, fields };
  },
  data() {
    return {
      info: null,
      userFiles: [],
    };
  },
  computed: {},
  methods: {},
  mounted() {
    axios
      .get("http://127.0.0.1:8000/files.json")
      .then((response) => (this.userFiles = response.data));
  },
};
</script>

<style scoped>
h1 {
  color: #fff;
}
</style>
