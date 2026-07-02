function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      {/* Top Navbar */}
      <header className="bg-blue-700 text-white p-4 flex justify-between items-center">
        <h1 className="text-xl font-bold">
          Student OS
        </h1>

        <button className="bg-orange-500 px-4 py-2 rounded">
          Logout
        </button>
      </header>

      {/* Main Content */}
      <main className="flex items-center justify-center h-[80vh]">
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold mb-4">
            Welcome to Student OS 🚀
          </h2>

          <p>
            React + Tailwind Shell Running Successfully
          </p>
        </div>
      </main>

      {/* Bottom Navigation */}
      <footer className="fixed bottom-0 w-full bg-white shadow-lg p-4 flex justify-around">
        <button>Home</button>
        <button>Events</button>
        <button>Notes</button>
        <button>Attendance</button>
      </footer>
    </div>
  );
}

export default App;