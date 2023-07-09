(ns web-scraper.core
  (:require [clj-http.client :as client]
            [cheshire.core :as json]
            [clojure.java.io :as io]))

(defn parse-page [body]
  ;; parsing logic here
  )

(defn save-json [data filename]
  (with-open [writer (io/writer filename)]
    (json/generate-stream data writer)))

(defn scrape-poe []
  (let [url "http://www.poe.com"
        response (client/get url)
        parsed-data (parse-page (:body response))]
    (save-json parsed-data "scraped_data.json")))

(defn -main []
  (scrape-poe))