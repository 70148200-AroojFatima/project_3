resource "local_file" "myfile" {
  filename = var.file_name
  content  = var.file_content
}