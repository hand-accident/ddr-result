<script>
    let className;
    export { className as class };
</script>

<footer class="c {className}">
    <slot />
</footer>

<style lang="postcss" module>
    .c {
        @apply footer bg-neutral text-neutral-content;
    }
</style>
