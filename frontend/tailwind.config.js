/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        niisBlue: "#0F52BA",
        niisOrange: "#FF7A00",
        niisGray: "#F4F4F4",
      },
    },
  },
  plugins: [],
}