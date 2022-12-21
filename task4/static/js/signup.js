// $(document).ready(function () {
//     $("#user-avatar").on('change', function () {
//         const file_name = $(this).val().replace(/^.*[\\\/]/, '')
//         $(this).next(".custom-file-label").text(file_name);
//     })
// })
// Пример стартового JavaScript для отключения отправки форм при наличии недопустимых полей
(function () {
  'use strict'

  // Получите все формы, к которым мы хотим применить пользовательские стили проверки Bootstrap
  var forms = document.querySelectorAll('.needs-validation')

  // Зацикливайтесь на них и предотвращайте отправку
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()