    const folderInput = document.getElementById("folderInput");
    const previewContainer = document.getElementById("previewContainer");
    const prediction = document.getElementById("prediction");
    const analysisPanel = document.getElementById("analysisPanel");

    folderInput.addEventListener("change", () => {
      const files = folderInput.files;
      previewContainer.innerHTML = "";
      analysisPanel.innerHTML = "";
      let results = [];

      Array.from(files).forEach((file, index) => {
        if (file.type.startsWith("image/")) {
          const reader = new FileReader();
          reader.onload = function(e) {
            const img = document.createElement("img");
            img.src = e.target.result;
            previewContainer.appendChild(img);

            const isReal = Math.random() > 0.5;
            const realScore = Math.floor(Math.random() * 41) + 60;
            const fakeScore = 100 - realScore;
            const label = isReal ? "Real" : "Fake";

            results.push(`${file.name}: ${label}`);

            const analysisBox = document.createElement("div");
            analysisBox.className = "analysis-box";
            analysisBox.innerHTML = `<strong>${file.name}</strong><br>Real: ${realScore}%<br>
            <div style="margin-top: 10px;">
                <div style="background: #d1fae5; border-radius: 8px; overflow: hidden; height: 16px;">
                  <div style="width: ${realScore}%; background: #10b981; height: 100%;"></div>
                </div>
            Fake: ${fakeScore}% <br>
                <div style="background: #fee2e2; border-radius: 8px; overflow: hidden; height: 16px;">
                  <div style="width: ${fakeScore}%; background: #ef4444; height: 100%;"></div>
                </div>
              </div>`;
            analysisPanel.appendChild(analysisBox);

            if (results.length === files.length) {
              prediction.innerHTML = results.join('<br>');
            }
          };
          reader.readAsDataURL(file);
        }
      });
    });