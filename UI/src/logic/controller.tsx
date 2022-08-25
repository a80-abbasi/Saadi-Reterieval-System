import axios from "axios";
import { clusteringApi, expansionAPi, linkanalysisApi, searchApi } from "./apis";
export const searchText = async (text: string, type: string) => {
  let n=10
  const res = await axios.get(searchApi, {
    params: { method: type, query: text, n: n },
  });
  return res.data;
};
export const clustringText = async (type: string, text?: string) => {
  const params = text ? { method: type, query: text } : { method: type };
  const res = await axios.get(clusteringApi, {
    params: params,
  });
  return res.data;
};

export const linkanalysisText = async (type: string) => {
  let n = 10;
  console.log("start");
  const res = await axios.get(linkanalysisApi, {
    params: { method: type, n: n },
  });
  console.log("end");

  return res.data;
};
export const expansionText = async (query: string) => {
  const res = await axios.get(expansionAPi, {
    params: { query: query, },
  });
  return res.data;
};
