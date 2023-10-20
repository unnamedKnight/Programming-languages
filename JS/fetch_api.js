// we have to add axios cdn as the top js script in our HTML file
// axios is promise based HTTP client

// simply we can make HTTP requests with axios and it returns a promise
// unlike .fetch() axios rejects promise based on HTTP error status code
// with axios we get the parsed data, which means we don't have
// to run .json() method on response
// parsing means converting data to one format to another
// for example, when we parse json data in js we get js objects

// axios
//   .get("https://swapi.dev/api/planets")
//   .then(({ data }) => {
//     const filmData = data.results[0];
//     // console.log(response.data.results.films[0])
//     const filmUrl = filmData.films[0];
//     return axios.get(filmUrl);
//   })
//   .then((response) => {
//     console.log(response.data.title);
//   })
//   .catch((err) => {
//     console.log("there is an error");
//   });

const test = () => {
  return new Promise((resolve, reject) => {
    const testVar = resolve();
    reject();
  });
};

test()
  .then(() => {
    console.log("I am resolved");
  })
  .catch((err) => {
    console.log("There is an error");
  });
