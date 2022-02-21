import create from "solid-zustand";
import type { Channel } from "../entities/Channel";

export interface State {
  channels: Channel[];
  addChannel: (channel: Channel) => void;
  removeChannel: (channelId: string) => void;
  updateChannel: (channel: Channel) => void;

  flashMessage: string | null;
  setFlashMessage: (message: string | null) => void;
  clearFlashMessage: () => void;
}

export const useStore = create<State>((set) => ({
  channels: [],
  addChannel: (channel) =>
    set((state) => ({ channels: [...state.channels, channel] })),
  removeChannel: (channelId) =>
    set((state) => ({
      channels: state.channels.filter((c) => c.channelId !== channelId),
    })),
  updateChannel: (channel) =>
    set((state) => ({
      channels: state.channels.map((c) =>
        c.channelId === channel.channelId ? channel : c
      ),
    })),

  flashMessage: null,
  setFlashMessage: (message) => set((state) => ({ flashMessage: message })),
  clearFlashMessage: () => set((state) => ({ flashMessage: null })),
}));
