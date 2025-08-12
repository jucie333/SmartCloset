Module.register("MMM-YourModule", {
    defaults: {
    },

    start: function() {
        this.imageData = null; // 이미지 데이터 저장
        this.sendSocketNotification("CONNECT", {});
    },

    socketNotificationReceived: function(notification, payload) {
        if (notification === "IMAGE_DATA") {
            this.imageData = payload;
            this.updateDom();
        }
    },

    getDom: function() {
        var wrapper = document.createElement("div");
        wrapper.className = "myContent";
        wrapper.innerHTML = "Hello, MagicMirror²!";

        if (this.imageData) {
            var img = document.createElement("img");
            img.src = `data:image/jpeg;base64,${this.imageData}`;
            wrapper.appendChild(img);
        }

        return wrapper;
    },

    notificationReceived: function(notification, payload, sender) {
    },

    socketNotificationReceived: function(notification, payload) {
        if (notification === "CONNECTED") {
            console.log("Connected to Python server!");
        }
    }
});
