import React from "react";
import IssueList from "./components/IssueList"; // Previously created component
import DepartmentList from "./components/DepartmentList"; // New component

function App() {
  return (
    <div className="App">
      <h1>My Django+React App</h1>
      {/* Display Departments */}
      <DepartmentList />
      {/* Optionally display Issues */}
      <IssueList />
    </div>
  );
}

export default App;