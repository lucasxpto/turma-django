/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      'core/templates/core/*.html',
      'core/templates/core/includes/*.html',
      'turma/templates/turma/*.html',
      'turma/templates/turma/includes/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [
      require('@tailwindcss/forms'),
  ],
}

