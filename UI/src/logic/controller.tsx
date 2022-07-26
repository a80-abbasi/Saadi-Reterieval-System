import axios from "axios";
import { clusteringApi, searchApi } from "./apis";
export const searchText = async (text: string, type: string, n?: 10) => {
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

export const linkanalysisText = async (type: string, n?: 10) => {
  const res = await axios.get(clusteringApi, {
    params: { method: type, n: n },
  });
  return res.data;
};
